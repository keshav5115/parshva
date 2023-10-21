from django.shortcuts import render,redirect
import pandas as pd
from app.models import Docket

# Create your views here.

def read_store_file():
    df = pd.read_csv('static\export29913.csv',encoding='utf-8', encoding_errors='ignore',)

    # Initialize a dictionary to store the data
    response_data = []
    suppliers=[]
    # Iterate through the rows of the DataFrame
    for index, row in df.iterrows():
        
        supplier = row['Supplier']
        print(supplier)
        if pd.notna(supplier):
            
            po_number = row['PO Number']
            description = row['Description']
            suppliers+=[supplier]
            
        else:
            
            supplier = suppliers[-1]
            description = row['Description']
            print(suppliers)
        
        properties =row
        data = {
            'supplier': supplier,
            'po_number':po_number,
            'description': description
        } 
        response_data+=[data]
    return response_data
        

def supplier_page(request):
    # queryset  = ProductOrder.objects.values('supplier').distinct()
    data = read_store_file()
    # print(data)
    supplier = [obj['supplier'] for obj in data ]
    supplier_values =[] 
    [supplier_values.append(item) for item in supplier if item not in supplier_values]
    context ={"supplier": supplier_values  }
    if request.method == 'POST':
        supplier = request.POST.get('supplier')
        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        hours = request.POST.get('hours')
        rate = request.POST.get('rate')
        # queryset = ProductOrder.objects.filter(supplier=supplier)
        po_numbers =[]
        for obj in data:
            if obj['supplier'] == supplier:
                if obj['po_number'] not in po_numbers:
                    po_numbers+=[obj['po_number']]
                
        
        # [ po_numbers.append(num.po_number)  for num in queryset if num.po_number not in po_numbers]
        # po_numbers = [num.po_number for num in query_numbers]
        
        
        
        context ={
        'po_numbers': po_numbers,
        'name':name, 
        'start_time':start_time, 
        'end_time':end_time,
        'hours':hours,
        'rate':rate,
        'supplier':supplier,
        }
        return render(request, 'ordertemp.html', context)
        
    return render(request, 'product.html', context)

def order_temp_page(request):
    if request.method == 'POST':
        supplier = request.POST.get('supplier')
        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        hours = request.POST.get('hours')
        rate = request.POST.get('rate')
        po_number = request.POST.get('po_number')
        data = read_store_file()
        # queryset = ProductOrder.objects.filter(po_number=po_number,supplier = supplier)
        description = []
        for obj in data:
            if obj['supplier'] == supplier and obj['po_number'] == po_number:
                description+=[obj['description']]
                
        
        
            
        Docket.objects.create(supplier=supplier,
                              description=description,
                              name=name,
                              start_time=start_time,
                              end_time = end_time,
                              hours=hours,
                              rate = rate,
                              po_number = po_number)
        
            
        
    return redirect('/docket/')