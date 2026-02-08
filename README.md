# AWS-Security-Auditor-v1.0 

🎯 Overview
AWS Security Auditor is a Python-based automated security scanning tool designed to identify common misconfigurations in Amazon Web Services (AWS) infrastructure. Built to address the critical industry need where 80% of data breaches involve cloud misconfigurations, this tool provides rapid vulnerability detection similar to commercial products like Prowler and AWS Security Hub.
Why This Matters

Capital One (2019): Misconfigured S3 bucket → 100M records exposed → $80M in fines
Uber (2016): Public S3 bucket → 57M users affected → $148M settlement
Industry Average: 287 days to detect a breach → This tool detects in < 5 seconds

✨ Features
Current Capabilities (v1.0)

✅ S3 Bucket Scanning

Public access detection (HIGH severity)
Encryption status validation (MEDIUM severity)
Versioning configuration check (LOW severity)


✅ Professional Reporting

Color-coded severity levels (RED/YELLOW/GREEN)
Detailed issue descriptions
Summary statistics
Actionable remediation guidance


✅ Security-First Design

Read-only IAM permissions
Secure credential management
No modification of infrastructure
AWS best practices compliance



🚀 Coming Soon (v2.0)

 IAM policy scanner (weak policies, missing MFA)
 EC2 security group analysis (open ports, 0.0.0.0/0 exposure)
 RDS database security (public accessibility, encryption)
 HTML report generation with charts
 Multi-account scanning support
 Scheduled automated scans

🛠️ Tech Stack
TechnologyPurposePython 3.14Core programming languageboto3AWS SDK for Python - API interactionAWS CLICredential management and authenticationColoramaTerminal color output for reports
📋 Prerequisites
Before you begin, ensure you have:

Python 3.8 or higher
AWS CLI 2.x installed
Active AWS account
IAM user with SecurityAudit policy (or equivalent read-only permissions)

🚀 Quick Start

1. Clone the Repository
bashgit clone (https://github.com/Frhnfaya/AWS-Security-Auditor-v1.0.git)

cd aws-security-auditor
3. Install Dependencies
bashpip install -r requirements.txt
4. Configure AWS Credentials
bashaws configure
# Enter your Access Key ID
# Enter your Secret Access Key  
# Default region: us-east-1
# Output format: json
4. Run Your First Scan
bashpython auditor.py
Expected Output
╔═══════════════════════════════════════╗
║   AWS Security Auditor v1.0          ║
║   S3 Bucket Security Scanner         ║
╚═══════════════════════════════════════╝

[*] Region: us-east-1
[*] Starting security audit...

[*] Starting S3 bucket scan...
[*] Found 2 bucket(s). Scanning...

==================================================
SECURITY ISSUES FOUND
==================================================

🔴 [HIGH] my-public-bucket
    Issue: Public Access Enabled
    Details: Bucket is publicly accessible to AllUsers

🟡 [MEDIUM] backup-bucket
    Issue: Encryption Not Enabled
    Details: Bucket does not have server-side encryption enabled

🟢 [LOW] logs-bucket
    Issue: Versioning Not Enabled
    Details: Bucket versioning is disabled (data recovery risk)

==================================================
SCAN SUMMARY
==================================================

Total Issues Found: 3
  High:   1
  Medium: 1
  Low:    1

⚠️  CRITICAL: 1 high-severity issue(s) found!

[*] Scan complete!
📁 Project Structure
aws-security-auditor/
├── auditor.py              # Main application entry point
├── config.py               # Configuration and settings
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── scanners/
│   ├── __init__.py
│   └── s3_scanner.py      # S3 bucket security checks
└── report/
    ├── __init__.py
    └── generator.py       # Report generation module
..................................................................................


🙏 Acknowledgments

Inspired by the need for accessible cloud security tools
Built to understand AWS security deeply, not just use existing tools
Thanks to the open-source security community for resources and knowledge

📞 Support
Found a bug? Have a question? Want to contribute?

Issues: GitHub Issues
Discussions: GitHub Discussions
Email: frhnh8635@gmail.com
