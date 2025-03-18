import sqlite3
conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos
               (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               ''')

def list_videos():
    print("\n")
    print("*" * 70 )
    print("\n")
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    
    print("\n")
    print("*" * 70 )

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name =?,time=? WHERE id = ?",(name,time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\nVideo manager with database please choose an option:")
        print("1. List Videos.")
        print("2. Add Videos.")
        print("3. Update Videos.")
        print("4. Delete Videos.")
        print("5. Exit App.")

        choice = input("Enter you choice: ")
        
        if choice == '1':
            list_videos()
            
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
            
        elif choice == '3':
            video_id = input("Enter the video id: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id,name,time)
            
        elif choice == '4':
            video_id = input("Enter the video id: ")
            delete_video(video_id)
        
        elif choice == '5':
            print("You have choosen Exit(). \nThank You for using app.")
            break
        
        else:
            print("Invalid Choice.")
    
    conn.close()
            

if __name__ == '__main__':
    main()