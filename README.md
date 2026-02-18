# 🛡️ Sentinel Core Security Gate

**The only deterministic enforcement engine that blocks insecure code before it hits production.**

## 🚀 Quick Start & Live Demo
Don't just read about it—test it yourself in our controlled environment:
👉 **[Try the Live Demo (the-stand)](https://github.com/DataWizual-Labs/the-stand)**

### 💡 Why Sentinel Core?
* **Deterministic**: No "maybe" or "low/high" risks. Only **ALLOW** or **BLOCK**.
* **Zero-Telemetry**: Your code never leaves your runner.
* **Hardware-Bound**: Enterprise security locked to your specific infrastructure.

---

# 🛡️ Sentinel Core — Client Demo Procedure (the-stand)

This demo uses a controlled GitHub repository called **`the-stand`** to demonstrate how **Sentinel Core** acts as a **Deterministic Security Enforcement Gate** inside a CI/CD pipeline.

It is not a passive scanner.
It produces a **hard security decision**: **PASS** or **BLOCK**.

---

## ✅ Client Instructions

### Step 1 — Access the Demo Repository

You will be granted access to:

**DataWizual-Labs/the-stand**

This repository is pre-configured with the Sentinel workflow:

```
.github/workflows/sentinel-check.yml
```

No installation is required on your side.

---

### Step 2 — Push Test Files Into the Repository

Add any **non-sensitive** code or infrastructure configuration you want to test, for example:

* `Dockerfile`
* Terraform `*.tf`
* GitHub Actions workflows

Push normally:

```bash
git add .
git commit -m "Sentinel security test"
git push origin main
```

That is all.

---

### Step 3 — Sentinel Executes Automatically

On every push or pull request, GitHub Actions triggers:

**Sentinel Security Gate**

Inside the CI runner, Sentinel runs:

```bash
sentinel scan . --report
```

---

### Step 4 — View the Security Result

Go to:

**GitHub → Actions tab → Sentinel Security Gate**

You will immediately see the enforcement outcome:

* 🟢 **Green (Success)** → No critical violations
* 🔴 **Red (Failure)** → Sentinel detected a blocker and stopped the pipeline

---

### Step 5 — Read the Decision Summary

A clear verdict is generated directly in the GitHub Job Summary.

Example:

```
Decision: BLOCK
Rule: SUPPLY-001
Issue: Mutable Docker tag 'node:latest' detected.
Action: Pin the image to a fixed version tag or SHA digest.
```

Sentinel does not only report — it enforces.

---

### Step 6 — Download the Full Audit Report

A full structured report is uploaded automatically:

**Artifacts → sentinel-security-reports**

Includes:

* Markdown summary
* HTML audit report
* Evidence + remediation steps

This provides compliance-grade documentation.

---

## ✅ What This Demo Proves

This GitHub stand demonstrates that Sentinel Core is a **Deterministic Enforcement Gate**, not a noisy scanner.

Sentinel Core:

* Detects critical security violations
* Produces audit-ready evidence
* Hard-blocks insecure changes before deployment

---

## 🚀 Production Deployment (Real-World Sentinel Core)

The GitHub stand is only the demonstration layer.

In production, Sentinel Core operates with maximum strictness:

* **Offline Execution (Zero-Telemetry)** — your code never leaves your perimeter
* **Local Enforcement** — blocks insecure commits before they ever reach CI
* **Administrator-Controlled Policies** — users cannot bypass the gate

Enterprise-grade security, fully deterministic.

---

**Sentinel Core = Security That Physically Stops Risk.**
