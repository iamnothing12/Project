# Ninjabot
 This project's purpose is to scrape websites to attempt to achieve identicality as close as possible to the WCAG Guidelines

## Linux/WSL Setup GUide
* `sudo apt update`
* `sudo apt-get -y install python3`
* `sudo apt-get -y install python3-pip`
* `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.* 3`
* `sudo pip3 install --upgrade pip`
* `sudo pip3 install bs4 selenium urllib3[secure] tldextract lxml`
* Note if `pip3` installation fails run `python -m pip install --user [package]`
* `sudo python -m pip install --user bs4 selenium urllib3[secure] tldextract lxml`

