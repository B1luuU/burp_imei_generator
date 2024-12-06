# Burp IMEI Brute Force Plugin  

## Overview  
This **Burp Suite Extension** is designed to generate and test large sets of IMEI (International Mobile Equipment Identity) numbers. It is particularly useful for brute-forcing IMEI-based security mechanisms, such as authentication or device-specific restrictions.  

## Features  
- **Generate Random IMEI Numbers:** Create valid IMEI numbers dynamically.  
- **Customizable Quantity:** Specify the number of IMEIs to generate.  
- **Integration with Burp Intruder:** Seamlessly use the generated IMEIs as payloads in Intruder attacks.  
- **Replace Values in Repeater:** Easily substitute selected values in the Repeater tab with generated IMEIs.  

## Requirements  
- Burp Suite (Community or Professional Edition).  
- Jython Standalone (if using Burp's legacy Python extension support).  

## Installation  

1. **Set up Jython (if needed):**  
   Download the [Jython standalone JAR](https://www.jython.org/download) and configure it in Burp Suite under:  
   `Extender > Options > Python Environment`.  

2. **Add the Plugin:**  
   - Clone or download this repository:  
     ```bash  
     git clone https://github.com/gustavorobertux/burp_imei_generator.git
     ```  
   - In Burp Suite, go to `Extender > Extensions > Add`.  
   - Select "Extension Type: Python" and load the `burp_imei_generator.py` file from the repository.  

3. **Verify Installation:**  
   The extension should appear under `Extender > Extensions`, and its functionality should now be accessible.  

## Usage  

### 1. Generating IMEIs  
- Open the **IMEI Generator** tab in Burp Suite.  
- Specify the number of IMEIs to generate or allow the generator to run until the attack stops.  
- Click **Generate** to start.  

### 2. Using with Intruder  
- Configure an attack in the **Intruder** tab.  
- Select "Payloads" and choose "Extension-generated" as the source.  
- Generated IMEIs will be used as payloads.  

### 3. Replacing IMEI in Repeater  
- Right-click a value in the **Repeater** tab.  
- Select "Replace with Generated IMEI".  

## License  
This project is licensed under the [MIT License](LICENSE).  

## Disclaimer  
This tool is intended for educational purposes and authorized testing only. Misuse of this tool may lead to legal consequences. The developers are not responsible for any misuse or damage caused.
