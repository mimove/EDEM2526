from initial_info import flights, passengers

def show_object_info(obj):


    # Handle list of dictionaries
    if isinstance(obj, list):
        for item in obj:
            for key, value in item.items():
                if key == "passengerIds":
                    print(f"{key}:")
                    for passenger_id, status in value:
                        print(f"  - {passenger_id}: {status}")
                else:
                    print(f"{key}: {value}")
            print("-" * 40)  # Add separator between flights


def flights_info():
    show_object_info(flights)

if __name__ == "__main__":
    # Print the flights data
    flights_info()
    print("Application finished successfully.")
