import os 
import csv

HTTP = [ "http://", "https://", "http://www.", "https://www." ]

#Source URL path
file_path = 'redirections.txt'

#URL save path
url_savepath = 'detailed_redirections.txt'

#Output CSV file path
output_file = 'output.csv'

#Shell script path
shell_script_path = 'curl.sh'

 
#Read initial URL list
def get_url(file_path):
  with open(file_path, 'r') as file: 
    urls = file.readlines()
  return urls


#Write detailed URL list to file
def write_url(url_savepath,url):
  with open ( url_savepath , mode="a") as f :
    f.write(url)


#Pass URLs and CSV file path to Shell program
def call_shell(url_savepath, output_file):
  os.system(f"{shell_script_path} {url_savepath} {output_file}")
  

# main function
def main():
  urls = get_url(file_path)
  for url in urls:
    source_url = url.split()[0]
    destination_url = url.split()[1]
    for http in HTTP:
      curl_url = http + source_url
      write_url(url_savepath, f"{curl_url} {destination_url} \n")
  
  call_shell(url_savepath, output_file)
    
  
if __name__ == "__main__":
  main()
