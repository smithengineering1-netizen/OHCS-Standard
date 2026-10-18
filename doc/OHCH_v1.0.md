# Open Hardware Conformance Standard (OHCS)
### Mixed‑Signal Finite State Controller (MS‑FSC)
Version 1.0 — October 2026

---

## 1. Purpose
The OHCS defines a universal, open‑source mixed‑signal finite state controller architecture for SMPS/PLC systems.  
It ensures multi‑vendor interoperability, deterministic digital behavior, and quantifiable mixed‑signal performance.

---

## 2. Architecture Overview
The MS‑FSC consists of:

1. FSM (Moore machine)
2. PWM generator
3. DSP48‑based control‑law module
4. ADC interface
5. Analog front‑end (741 op‑amp + RLC filter)
6. SMPS plant model

Closed loop:
FSM → PWM → SMPS → Analog Conditioning → ADC → FSM

---

## 3. Digital Interface Specification

### Mandatory Ports
| Signal | Dir | Description |
|--------|-----|-------------|
| clk_sys | in | 100 MHz system clock |
| rst_n | in | Active‑low reset |
| start | in | Start command |
| fault | in | External fault |
| adc_start | out | ADC conversion request |
| adc_done | in | ADC conversion complete |
| adc_data[N-1:0] | in | ADC result |
| pwm_out | out | PWM gate drive |
| err_in[17:0] | out | DSP error input |
| k_gain[17:0] | in | DSP gain coefficient |
| dsp_valid_in | out | DSP input strobe |
| dsp_valid_out | in | DSP output strobe |
| dsp_u_out[47:0] | in | DSP output |

---

## 4. FSM Specification

### States
- S_IDLE  
- S_MEAS  
- S_COMP  
- S_UPDATE  
- S_FAULT  

### Rules
- S_MEAS → assert adc_start, wait for adc_done  
- S_COMP → compute control law using DSP48  
- S_UPDATE → apply new duty cycle  
- S_FAULT → latch fault, disable PWM  

---

## 5. Timing Specification

### Clock Requirements
- clk_sys = 100 MHz  
- clk_pwm = 200 kHz–1 MHz  
- clk_adc = 10–100 kHz  

### Latency Requirements
- ADC‑to‑PWM update latency ≤ 5 cycles  
- PWM duty updates only at period boundaries  
- DSP48 pipeline latency must be declared  

---

## 6. KPI Thresholds

| KPI | Definition | Threshold |
|-----|------------|-----------|
| Aliasing RMS | RMS(Vout − Vadc) | ≤ 5% of Vref |
| Bit Error RMS | RMS(Vadc − Videal) | ≤ 1% of Vref |
| Leakage Probability | Unexpected output changes | ≤ 1e‑3 |
| Leakage CI95 Upper Bound | 95% confidence interval | ≤ 5e‑3 |

---

## 7. Conformance Tests

### Functional Test
Verify FSM transitions, PWM updates, fault handling.

### Aliasing Test
Run Simulink mixed‑signal model at multiple sampling frequencies.

### Bit Error Test
Compare ADC output vs ideal reference.

### Leakage Test
Hold inputs constant and detect unintended output changes.

### Confidence Interval Calculation
Use automated MATLAB report generator.

---

## 8. Vendor Deliverables

- RTL or netlist  
- Timing report  
- KPI report  
- Testbench results  
- Simulink/Vivado logs  

---

## 9. Certification

Vendor receives:

**PASS** — fully conformant  
**FAIL** — non‑conformant  

---

## 10. License
MIT License — open for commercial and academic use.

