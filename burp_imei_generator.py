# -*- coding: utf-8 -*-

from burp import IBurpExtender, IContextMenuFactory, IIntruderPayloadGeneratorFactory, IIntruderPayloadGenerator, IMessageEditorTabFactory
from javax.swing import JMenuItem
from java.awt.event import ActionListener
import random

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("IMEI Generator")
        callbacks.registerIntruderPayloadGeneratorFactory(self)
        callbacks.registerContextMenuFactory(self)
        print("IMEI Generator Extension for Intruder and Repeater registered")

    def getGeneratorName(self):
        return "IMEI Payload Generator"

    def createNewInstance(self, attack):
        return ImeiPayloadGenerator()

    # Context menu for Repeater
    def createMenuItems(self, invocation):
        menu_item = JMenuItem("Replace with Generated IMEI", actionPerformed=lambda x: self.replace_with_imei(invocation))
        return [menu_item]

    def replace_with_imei(self, invocation):
        selected_text = invocation.getSelectedMessages()[0]
        request_info = self._helpers.analyzeRequest(selected_text)
        request_bytes = selected_text.getRequest()

        # Generate new IMEI
        imei = ImeiPayloadGenerator().generate_imei()
        selected_offset = invocation.getSelectionBounds()
        
        # Replace selected text with generated IMEI
        new_request = request_bytes[:selected_offset[0]] + self._helpers.stringToBytes(imei) + request_bytes[selected_offset[1]:]
        selected_text.setRequest(new_request)

class ImeiPayloadGenerator(IIntruderPayloadGenerator):
    def __init__(self):
        self._generated_count = 0  # Count of generated IMEIs

    def hasMorePayloads(self):
        # Always return True for unlimited IMEI generation
        return True

    def getNextPayload(self, baseValue):
        # Generate the next IMEI
        imei = self.generate_imei()
        self._generated_count += 1
        return imei

    def reset(self):
        self._generated_count = 0

    def generate_imei(self):
        # Generate the first 14 digits
        imei_base = [random.randint(0, 9) for _ in range(14)]
        
        # Calculate the check digit
        check_digit = self.calculate_luhn(imei_base)
        imei_base.append(check_digit)
        
        # Return IMEI as a string
        return ''.join(map(str, imei_base))

    def calculate_luhn(self, digits):
        sum_digits = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                sum_digits += digit
            else:
                doubled = digit * 2
                sum_digits += doubled if doubled < 10 else doubled - 9
        return (10 - (sum_digits % 10)) % 10

