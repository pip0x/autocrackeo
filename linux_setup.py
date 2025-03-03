try:
	import wget, os
	import zipfile
	import py7zr
	import gzip
	import shutil
	import bz2

except Exception as e:
	print("Import wget module!")
	print("[X] Exception: " + e)



def check_disk_space(required_gb=10):
    """Checks if there is enough free disk space."""
    total, used, free = shutil.disk_usage(".")  # Get disk space where the script is running
    free_gb = free / (1024 ** 3)  # Convert bytes to GB

    if free_gb < required_gb:
        print(f"Error: Insufficient disk space. {required_gb} GB required, but only {free_gb:.2f} GB available.")
        sys.exit(1)  # Exit script with error code

    print(f"Sufficient disk space: {free_gb:.2f} GB available.")


def download_files(files, directory):

	if os.path.exists(directory):
		for file in files.items():
			filename = file[0]
			url = file[1]
			print("\n\nDownloading from URL: " + url)
			path = os.path.join(directory,filename)
			try:
				wget.download(url, path)
				print("\nSaved in " + path)
			except KeyboardInterrupt as e:
				print("\n[!] Skipping...")
			except Exception as e:
				print("[X] " + str(e))
	else:
		print("\n[X] Folder " + directory + " does not exist...")

def unzip_files(directory):
    """Extracts .zip, .7z, .gz, and .bz2 files in the given directory."""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        try:
            if filename.endswith('.zip'):
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                    zip_ref.extractall(directory)
                print(f"Extracted {filename} in {directory}")

            elif filename.endswith('.7z'):
                with py7zr.SevenZipFile(filepath, mode='r') as z:
                    z.extractall(directory)
                print(f"Extracted {filename} in {directory}")

            elif filename.endswith('.gz'):
                output_filepath = os.path.splitext(filepath)[0]  # Remove .gz extension
                with gzip.open(filepath, 'rb') as f_in, open(output_filepath, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                print(f"Extracted {filename} to {output_filepath}")            

            elif filename.endswith('.bz2'):
                output_filepath = os.path.splitext(filepath)[0]  # Remove .bz2 extension
                with bz2.BZ2File(filepath, 'rb') as f_in, open(output_filepath, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                print(f"Extracted {filename} to {output_filepath}")

        except Exception as e:
            print(f"Error extracting {filename}: {e}")


        except (zipfile.BadZipFile, py7zr.Bad7zFile, gzip.BadGzipFile, OSError, IOError) as e:
            print(f"[X] Failed to extract {filename}: {str(e)}")

print("[*] This uses command line 7zip decompressing program: https://www.7-zip.org/download.html")

print("[*] Donwlading external files... Ctrl + C to skip current file download")


rules = {
	"hob064.rule": "https://raw.githubusercontent.com/praetorian-code/Hob0Rules/master/hob064.rule",
	"rockyou-30000.rule": "https://raw.githubusercontent.com/hashcat/hashcat/master/rules/rockyou-30000.rule",
	"T0XlC.rule": "https://raw.githubusercontent.com/hashcat/hashcat/master/rules/T0XlC.rule",
    #new
    #-----------
    "T0XlC_3_rule.rule": "https://raw.githubusercontent.com/hashcat/hashcat/master/rules/T0XlC_3_rule.rule",
	"best66.rule": "https://raw.githubusercontent.com/hashcat/hashcat/master/rules/best66.rule",
    "top10_2023.rule": "https://raw.githubusercontent.com/hashcat/hashcat/master/rules/top10_2023.rule",
	#-----------
    "d3ad0ne.rule": "https://raw.githubusercontent.com/hashcat/hashcat/master/rules/d3ad0ne.rule",
	"toggles-lm-ntlm.rule": "https://raw.githubusercontent.com/trustedsec/hate_crack/master/rules/toggles-lm-ntlm.rule",
	"OneRuleToRuleThemAll.rule": "https://raw.githubusercontent.com/NotSoSecure/password_cracking_rules/master/OneRuleToRuleThemAll.rule",
    "OneRuleToRuleThemStill.rule": "https://raw.githubusercontent.com/stealthsploit/OneRuleToRuleThemStill/refs/heads/main/OneRuleToRuleThemStill.rule",
	"haku34K.rule": "https://raw.githubusercontent.com/kaonashi-passwords/Kaonashi/master/rules/haku34K.rule",
	"kamaji34K.rule": "https://raw.githubusercontent.com/kaonashi-passwords/Kaonashi/master/rules/kamaji34K.rule",
	"yubaba64.rule": "https://raw.githubusercontent.com/kaonashi-passwords/Kaonashi/master/rules/yubaba64.rule",
    #pantagrule
    #v5
    "pantagrule.private.v5.hybrid.rule.gz": "https://github.com/rarecoil/pantagrule/raw/refs/heads/master/rules/private.v5/pantagrule.private.v5.hybrid.rule.gz",
    "pantagrule.private.v5.popular.rule.gz": "https://github.com/rarecoil/pantagrule/raw/refs/heads/master/rules/private.v5/pantagrule.private.v5.popular.rule.gz",
    "pantagrule.private.v5.random.rule.gz": "https://github.com/rarecoil/pantagrule/raw/refs/heads/master/rules/private.v5/pantagrule.private.v5.random.rule.gz",
    #v6
    "pantagrule.hashorg.v6.hybrid.rule.gz": "https://github.com/rarecoil/pantagrule/raw/refs/heads/master/rules/hashesorg.v6/pantagrule.hashorg.v6.hybrid.rule.gz",
    "pantagrule.hashorg.v6.popular.rule.gz": "https://github.com/rarecoil/pantagrule/raw/refs/heads/master/rules/hashesorg.v6/pantagrule.hashorg.v6.popular.rule.gz",
    "pantagrule.hashorg.v6.random.rule.gz": "https://github.com/rarecoil/pantagrule/raw/refs/heads/master/rules/hashesorg.v6/pantagrule.hashorg.v6.random.rule.gz"

}

masks = {
	"kaonashi.hcmask": "https://raw.githubusercontent.com/kaonashi-passwords/Kaonashi/master/masks/kaonashi.hcmask",
	#"2015-Top40-Time-Sort.hcmask": "https://blog.netspi.com/wp-content/uploads/2016/01/2015-Top40-Time-Sort.hcmask",
	"pathwell.hcmask": "https://raw.githubusercontent.com/trustedsec/hate_crack/master/masks/pathwell.hcmask",
	"rockyou-1-60.hcmask": "https://raw.githubusercontent.com/hashcat/hashcat/master/masks/rockyou-1-60.hcmask"
}

wordlists = {
	"google-10000-english.txt": "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt",
	"Password_Default_ProbWL.txt": "https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Dictionary-Style/Technical_and_Default/Password_Default_ProbWL.txt",
	"probable-v2-wpa-top4800.txt": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/WiFi-WPA/probable-v2-wpa-top4800.txt",
	"rockyou.txt.bz2": "http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2",    
	#"hashkiller.7z": "https://hashkiller.io/downloads/hashkiller-dict-2020-01-26.7z",
	"crackstation-human-only.txt.gz": "https://crackstation.net/files/crackstation-human-only.txt.gz",
    #Tiny > 1MB
    "rockyou-65.txt.gz": "https://weakpass.com/download/87/rockyou-65.txt.gz",
    "ignis-10K.txt.7z": "https://weakpass.com/download/1934/ignis-10K.txt.7z",
    "rockyou-60.txt.gz": "https://weakpass.com/download/86/rockyou-60.txt.gz",
    "10_million_password_list_top_10000.txt.gz": "https://weakpass.com/download/48/10_million_password_list_top_10000.txt.gz",
    #Small > 100MB
    "hashmob.net.small.found.txt.7z": "https://weakpass.com/download/1987/hashmob.net.small.found.txt.7z",
    #Medium > 500MB
    "hk_hlm_founds.txt.gz": "https://weakpass.com/download/1256/hk_hlm_founds.txt.gz",
    "kaonashi14M.txt.7z": "https://weakpass.com/download/1938/kaonashi14M.txt.7z",
    "ignis-10M.txt.7z": "https://weakpass.com/download/1935/ignis-10M.txt.7z",
    "piotrcki-wordlist-top10m.txt.7z": "https://weakpass.com/download/2020/piotrcki-wordlist-top10m.txt.7z",
    #BIG < 1GB
    "cyclone_hk.txt.7z": "https://weakpass.com/download/1928/cyclone_hk.txt.7z",
    "hashmob.net.large.found.txt.7z": "https://weakpass.com/download/1981/hashmob.net.large.found.txt.7z",
    "hashkiller-dict.txt.7z": "https://weakpass.com/download/1932/hashkiller-dict.txt.7z"
    
    #https://weakpass.com/download/1939/kaonashi.txt.7z
      
}

check_disk_space()
base_dir = os.path.dirname(os.path.realpath(__file__))

download_files(rules, os.path.join(base_dir, "rules"))
download_files(masks, os.path.join(base_dir, "masks"))
download_files(wordlists, os.path.join(base_dir, "wordlists"))

unzip_files(os.path.join(base_dir, "rules"))
unzip_files(os.path.join(base_dir, "wordlists"))

#print("\n\n\n\n[-->] TODO: extract rockyou.txt.bz2 --> \"C:\\Program Files\\7-Zip\\7z.exe\" x rockyou.txt.bz2")
#print("\n[-->] TODO: extract hashkiller-dict-2020-01-26.7z --> \"C:\\Program Files\\7-Zip\\7z.exe\" x hashkiller-dict-2020-01-26.7z")
#print("\n[-->] TODO: extract crackstation-human-only.txt.gz --> \"C:\\Program Files\\7-Zip\\7z.exe\" x crackstation-human-only.txt.gz")
#print("\n[-->] TODO: download from mega or torrent Kaonashi14M --> https://github.com/kaonashi-passwords/Kaonashi/tree/master/wordlists and extract the wordlist: 7za e kaonashi14M.7z")