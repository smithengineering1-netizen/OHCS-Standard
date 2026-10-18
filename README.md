# Open Hardware Conformance Standard (OHCS)
### Mixed‑Signal Finite State Controller (MS‑FSC)
Version 1.0 — October 2026  
Maintainer: Jimmy Willard Anthony Smith (Clarkson EE ’99)

---

## Overview
The Open Hardware Conformance Standard (OHCS) defines a vendor‑neutral, mixed‑signal finite state controller (MS‑FSC) architecture for SMPS/PLC applications.  
It ensures interoperability across FPGA, ASIC, SPLD, CPLD, GPU‑accelerated, and photonic‑hybrid controllers.

This repository contains:
- Reference RTL (FSM, PWM, DSP control law)
- Mixed‑signal Simulink model
- MATLAB KPI analysis scripts
- Vendor onboarding kit
- Automated CI/CD conformance testing

---

## Repository Structure

---

## Conformance Summary

A vendor implementation is **certified PASS** if:
- Aliasing RMS ≤ 5% of Vref  
- Bit Error RMS ≤ 1% of Vref  
- Leakage Probability ≤ 1e‑3  
- Leakage CI95 Upper Bound ≤ 5e‑3  
- All functional FSM/PWM/ADC tests pass  

Otherwise, the vendor receives **FAIL**.

---

## How Vendors Submit

1. Fork this repository  
2. Add RTL + timing report  
3. Add Simulink/Vivado co‑simulation logs  
4. Run CI locally  
5. Submit pull request  

The CI/CD pipeline automatically evaluates conformance.

---

## License
MIT License — open for commercial and academic use.

