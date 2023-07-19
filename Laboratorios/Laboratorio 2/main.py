# metodo sin concurrencia

'''import api
import ids
import time

def main():
    start_time = time.time()

    for number in ids.ids:
        user_data = api.getOneUser(number)
        print(user_data['name'])

    end_time = time.time()
    print("Time taken:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()
'''    


# main.py
import api
import ids
import time
import concurrent.futures

def fetch_user_data(number):
    user_data = api.getOneUser(number)
    return user_data['name']

def main():
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(fetch_user_data, ids.ids)

    for name in results:
        print(name)

    end_time = time.time()
    print("Time taken:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()
