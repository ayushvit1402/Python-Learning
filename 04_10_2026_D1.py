#1.
'''
E-Commerce Inventory & Order Processor
'''
def process_order(inv ,ord_list):
    total_bill = 0
    for item in ord_list:
        if item in inv:
            price,stock = inv[item]
            if stock>0:
                total_bill+=price
                inv[item]=(price,stock-1)
    return total_bill,inv

inventory = {
    "Laptop": (50000,2),
    "Mouse": (500,5),
    "Keyboard": (1500,0)}

order_list=["Laptop","Mouse","Keyboard","Headphones"]

total, updated_inv= process_order(inventory,order_list)
print("Total Bill:",total)
print("Updated Inventory:",updated_inv)

#2.
'''
Unique Customer Analytics
'''
def analize_traffic(logs):
    city_users = {}
    for log in logs:
        u_id,city = log.split(":")
        if city not in city_users:
            city_users[city] = set()
        city_users[city].add(u_id)
    result={}
    for city, setu_id in city_users.items():
        result[city]=len(setu_id)

    return result

log = ["user1:Mumbai","user2:Delhi","user1:Mumbai","user3:Delhi","user4:Mumbai"]

print(analize_traffic(log))

#3.
'''

'''
def get_top_student(gradebook):
    t_student = ""
    high_avg = 0.0
    for name,marks in gradebook.items():
        avg=sum(marks)/len(marks)
        if avg > high_avg:
            high_avg = avg
            t_student=name
    
    return t_student,round(high_avg,2)

gb={
    "Rohan":[80,90,85],
    "Priya":[95,92,98],
    "Rohan":[70,75,80],
}
print(get_top_student(gb))


         
