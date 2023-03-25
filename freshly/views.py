from django.shortcuts import render
from sqlalchemy import create_engine, insert
import qrcode
from freshly.models import Items
import uuid
import os


def create_new_page(item_id, item_name, item_description, portion_kcal, how, producer_name, path):
    with open(os.getcwd() + f"\\freshly\\items\\{item_id}_{item_name}.html", "w+") as f:
        f.write(f"""
            <!DOCTYPE html>        
            <html>
                <head>
                    <title> Product {item_name} !</title>
                </head>
                
                <body>
                    Item name: {item_name} <br>
                    Item description: {item_description} <br>
                    Calories per 100g (1 serving): {portion_kcal} <br>
                    How it was produced?: {how} <br>
                    Who produced this item?: {producer_name} <br>
                    QR CODE: <br>
                    <img src="{path}\\freshly\\items\\qr_codes\\{item_id}_{item_name}.jpg" alt="{item_name}">
                </body>
            </html>
        """)


def item_upload(request):
    db = create_engine('postgresql+psycopg2://postgres:c@localhost:5432/freshly_db').connect()
    print(request)
    if request.method == 'POST':
        item_id = uuid.uuid4()
        item_name = request.POST['item_name']
        item_description = request.POST['item_description']
        portion_kcal = request.POST['portion_kcal']
        how = request.POST['how']
        producer_name = request.POST['producer_name']
        
        db.execute(
            insert(Items)
            .values(
                item_id=item_id,
                item_name=item_name,
                item_description=item_description,
                portion_kcal=portion_kcal,
                how=how,
                producer_name=producer_name,
            )
        )
        db.commit()
        
        img = qrcode.make(os.getcwd() + f"\\freshly\\items\\{item_id}_{item_name}.html")
        img.save(os.getcwd() + f"\\freshly\\items\\qr_codes\\{item_id}_{item_name}.jpg")
        img.save(os.getcwd() + f"\\freshly\\static\\last_qr_code.jpg")
        create_new_page(item_id, item_name, item_description, portion_kcal, how, producer_name, os.getcwd())
        
        return render(request, 'success.html')
    else:
        return render(request, 'main_page.html')



# def logout_view(request):
#     logout(request)
#     return redirect('login')

