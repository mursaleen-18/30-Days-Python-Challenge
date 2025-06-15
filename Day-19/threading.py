import threading
import requests
import time

# List of sample file URLs (replace these with actual downloadable links)
urls = [
    "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip",
    "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-large-zip-file.zip",
    "https://file-examples.com/storage/fe45fc9492a5b17dc6e91dc/2017/10/file-sample_150kB.pdf",
]

def download_file(url):
    local_filename = url.split('/')[-1]
    print(f"Starting download: {local_filename}")
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    print(f"Finished download: {local_filename}")

# Track time
start = time.time()

# Create and start threads
threads = []
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end = time.time()
print(f"\nAll downloads completed in {round(end - start, 2)} seconds.")
