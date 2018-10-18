import re, urllib, argparse, os, os.path, glob, random

parser = argparse.ArgumentParser(description='RL')
parser.add_argument('--data', default='./data/data.txt',
                    help='(default: ./data/data.txt) Data file downloaded using searchme. Should be filtered to contain only messages with image and video attachments')
parser.add_argument('--destination', default='./dump/',
                    help='(default: ./dump/) folder to dump all downloaded attachments')
args = parser.parse_args()

def extract_urls(fname, regex):
    for line in open(fname, 'r+'):
        urls = re.findall(regex, line)
    return urls

def download_attachments(urls, destination):
    for i in reversed(range(len(urls))):
        print("{:5.2f}".format(float(len(urls)-i-1)/len(urls)*100)+" percent complete")
        url = urls[i].split(':', 1)[1].strip('\"')
        extension = get_file_type(url)
        urllib.urlretrieve(url, os.path.join(destination, str((len(urls)-1)-i).zfill(7)+"_attachment_"+str(random.randint(0, 1000000))+extension))

def get_file_type(url):
    if 'png' in url:
        return '.png'
    elif 'jpg' in url or 'jpeg' in url:
        return '.jpg'
    elif 'gif' in url:
        return '.gif'
    elif 'mp4' in url:
        return '.mp4'
    return ""

if __name__=='__main__':
    #attachment urls take the form "url":"address"
    regex = "\"url\":\".*?\""

    #check if destination director exists
    #if it does, empty it
    try:
        os.makedirs(args.destination)
    except OSError:
        files = glob.glob(os.path.join(args.destination, '*.*'))
        for f in files:
            os.remove(f)

    urls = extract_urls(args.data, regex)
    download_attachments(urls, args.destination)
    