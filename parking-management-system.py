parking ={}
total_slots = 5

while True:
    print("\n === Parking Management System ===")
    print("1.'park Vehicle'\n 2.'Remove Vehicle'\n3.'View Vehicle'\n 4.Available Vehicle'\n 5.'Exit'")
    
    choice = input("Enter choice:")
    
    if choice == "1":
        if len(parking) < total_slots:
            vehicle = input("Enter vehicle number: ")

            if vehicle in parking:
                print("Vehicle already parked!")
            else:
                for slot in range(1, total_slots + 1):
                    if slot not in parking.values():
                        parking[vehicle] = slot
                        print("Vehicle parked at slot", slot)
                        break
            
    elif choice =="2":
        vehicle =input("Enter vehicle number:")
        
        if vehicle in parking:
            slot =parking.pop(vehicle)
            print("Vehicle removed from slot",slot)
            
        else:
            print("Vehicle not Found!")
    
    elif choice =="3":
        if parking:
            print("\n parked Vehicles:")
            for vehicle, slot in parking.items():
                print("slot",slot,":",vehicle)
        
        else:
            print("No vehicles parked.")
            
    elif choice =="4":
        print("Available Slots:",total_slots- len(parking))
        
    elif choice =="5":
        print("Thank You!")
        break
    
    else:
        print("Invalid choice!")