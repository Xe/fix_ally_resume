#!/usr/bin/env bash

modprobe acpi_call
echo '\_SB.PCI0.SBRG.EC0.CSEE 0xb7' | tee /proc/acpi/call; cat /proc/acpi/call
sleep 0.3
echo '\_SB.PCI0.SBRG.EC0.CSEE 0xb8' | tee /proc/acpi/call; cat /proc/acpi/call
systemctl restart hhd@xe.service
