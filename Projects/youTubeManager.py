import json

filename = 'youtube.txt'
def load_data():
    try:
        with open(filename,'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(filename , 'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. Video name: {video['name']}, Duration: {video['time']} ")
    print('\n')
    print('*' * 70)
             
def add_video(videos):
    name = input("Enter a video name: ")
    time = input("Enter a video time: ")
    videos.append({'name':name , 'time':time})
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected.")
    
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected.")

def main():
    videos = load_data()
    while True:
        print("\n YouTubr Manager | Choose a option.")
        print("1. List all youtube videos.")
        print("2. Add a  youtube videos.")
        print("3. Update youtube videos details.")
        print("4. Delete youtube videos.")
        print("5. Exit the app.")
        
        choice = input("Enter your choice: ")
        # print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos) 
                
            case '2':
                add_video(videos) 
                
            case '3':
                update_video(videos) 
                
            case '4':
                delete_video(videos) 
                
            case '5':
                break 
            case _:
                print("Invalid Choice.")


if __name__ == '__main__':
    main()