from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from app.models import ProductOrder, Docket

# Create your views here.

def read_stor_file(request):
    df = pd.read_csv('static\export29913.csv',encoding='utf-8', encoding_errors='ignore',)

    # Initialize a dictionary to store the data
    
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
        
        # order=ProductOrder(
        #     supplier=supplier, 
        #     description=description,
        #     po_number=po_number,
        #     properties = properties
        #     )
        # order.save()
    return HttpResponse('records has inserted successfully')




def product_page(request):
    queryset  = ProductOrder.objects.values('supplier').distinct()
    supplier_values = [item['supplier'] for item in queryset]
    context ={"supplier": supplier_values  }
    if request.method == 'POST':
        supplier = request.POST.get('supplier')
        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        hours = request.POST.get('hours')
        rate = request.POST.get('rate')
        queryset = ProductOrder.objects.filter(supplier=supplier)
        po_numbers =[]
        [ po_numbers.append(num.po_number)  for num in queryset if num.po_number not in po_numbers]
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
        return render(request, 'order.html', context)
        
    return render(request, 'product.html', context)

def order_page(request):
    if request.method == 'POST':
        supplier = request.POST.get('supplier')
        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        hours = request.POST.get('hours')
        rate = request.POST.get('rate')
        po_number = request.POST.get('po_number')
        queryset = ProductOrder.objects.filter(po_number=po_number,supplier = supplier)
        description=[]
        for desc in queryset:
            description += [desc.description]
            
        Docket.objects.create(supplier=supplier,
                              description=description,
                              name=name,
                              start_time=start_time,
                              end_time = end_time,
                              hours=hours,
                              rate = rate,
                              po_number = po_number)
        
            
        
    return redirect('/docket/')
    
    
    
def docketVW(request):
    queryset =Docket.objects.all()
    return render(request,'docket.html',{'queryset':queryset})
    
    
