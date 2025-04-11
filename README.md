# HP Data Protector 8.10 Remote Command Execution Exploit

## 📅 Date
July 11, 2014

## ✍️ Exploit Authors
- **Christian (Polunchis) Ramirez** — [https://intlabs.ca](https://intlabs.ca)  
- **Henoch (Chan0c) Barrera** — [https://intlabs.ca](https://intlabs.ca)

**Contacts:**  
- polunchis@intlabs.ca  
- chanoc@intlabs.ca  

## 📦 Software Information
- **Affected Software:** HP Data Protector Manager 8.10 (latest version at the time)
- **Vendor Website:** [HP Data Protector](http://www8.hp.com/mx/es/software-solutions/software.html?compURI=1175640#.U8DhWaU_BjF)

## 🖥️ Tested On
- Windows Server 2003 (all languages)
- Windows Server 2008 (all languages)
- Windows Server 2012 (all languages)

## 🙏 Special Thanks
To GOD for giving us wisdom.

## 🛡️ Vulnerability Description
A **remote command execution (RCE)** vulnerability was discovered in **HP Data Protector Manager 8.10**.  
An attacker can execute arbitrary commands on the target system by sending a specially crafted request to **TCP port 5555**.

When the vulnerable service receives a crafted command, it improperly processes the input, leading to the execution of system-level commands under the privileges of the service.

## ⚙️ Exploitation Details
- **Vulnerability Type:** Remote Command Execution
- **Port:** 5555/TCP
- **Attack Vector:** Remote
- **Authentication:** Not required

## 🛠️ Usage
⚠️ **Warning:**  
This exploit is for educational purposes only. Unauthorized access to systems without permission is illegal.

```bash
# Example usage (to be filled if you provide a script)
python exploit.py --target <IP_ADDRESS> --command "<COMMAND>"
