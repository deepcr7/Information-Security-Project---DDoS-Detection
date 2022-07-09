"""
Testing all the Protocols with the attributes
"""
import numpy as np
import sys
import pickle
    
def icmp_test(attributes):
    model = pickle.load(open("./saved_model/icmp_data.sav", 'rb'))
    result = model.predict([attributes])
    if result == 0: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: IPSWEEP!")
    if result == 1: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: MULTIHOP!")
    if result == 2: 
        print("Predicted Label", result)
        print("There is no Attack taking place! Everything is NORMAL!")
    if result == 3: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: POD!")
    if result == 4: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SAINT")
    if result == 5: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SATAN!")
    if result == 6: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SMURF!")
    if result == 7: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SNMPGUESS!")
        
def udp_test(attributes):
    model = pickle.load(open("./saved_model/udp_data.sav", 'rb'))
    result = model.predict([attributes])
    if result == 0: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: MULTIHOP!")
    if result == 1: 
        print("Predicted Label", result)
        print("There is no Attack taking place! Everything is NORMAL!")
    if result == 2: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SAINT")
    if result == 3: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SATAN!")
    if result == 4: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SNMPGETATTACK!")
    if result == 5: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SNMPGUESS!")
    if result == 6: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: TEARDROP!")
    if result == 7: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: UDPSTORM!")

def tcp_syn_test(attributes):
    model = pickle.load(open("./saved_model/tcp_syn_data.sav", 'rb'))
    result = model.predict([attributes])
    if result == 0: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: APACHE2!")
    if result == 1: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: GUESS_PASSWD!")
    if result == 2: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: LAND!")
    if result == 3: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: MSCAN!")
    if result == 4: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: NEPTUNE!")
    if result == 5: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: NMAP!")
    if result == 6: 
        print("Predicted Label", result)
        print("There is no Attack Going on! Everything is NORMAL!")
    if result == 7: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: PROCESSTABLE!")
    if result == 8: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SAINT!")
    if result == 9: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: SATAN!")
    if result == 10: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: WAREZMASTER!")
    if result == 11: 
        print("Predicted Label", result)
        print("There is a DDoS Attack Going on! The type of Attack is: XSNOOP!")

if __name__ == "__main__":
    if sys.argv[1] == "icmp": 
        icmp_test(sys.argv[2:])
    elif sys.argv[1] == "tcp_syn":
        tcp_syn_test(sys.argv[2:])
    elif sys.argv[1] == "udp":
        udp_test(sys.argv[2:])
    else:
        sys.exit("Incorrect protocol has been chosen for testing. Try again.")