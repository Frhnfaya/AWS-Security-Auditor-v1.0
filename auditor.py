 #!/usr/bin/env python3
"""
AWS Security Auditor
A tool to scan AWS environments for security misconfigurations
"""

import sys
from scanners.s3_scanner import S3Scanner
from config import COLORS, SEVERITY, AWS_REGION

def print_banner():
    """Print tool banner"""
    banner = """
    ╔═══════════════════════════════════════╗   
    ║   AWS Security Auditor v1.0           ║  Cybersecurity Student| Security Researcher 
    ║   S3 Bucket Security Scanner          ║  | AWS | Cloud Security Enthusiast
    ║   Developed by  FARHAN FAYA           ║
    ╚═══════════════════════════════════════╝
    """
    print(COLORS['INFO'] + banner + COLORS['RESET'])

def print_issue(issue):
    """Print a single security issue with color"""
    severity = issue['severity']
    color = COLORS.get(severity, COLORS['RESET'])
    
    print(f"\n{color}[{SEVERITY[severity]}] {issue['bucket']}")
    print(f"    Issue: {issue['issue']}")
    print(f"    Details: {issue['description']}")
    print(COLORS['RESET'])

def print_summary(issues):
    """Print summary of findings"""
    print("\n" + "="*50)
    print("SCAN SUMMARY")
    print("="*50)
    
    # Count by severity
    high = len([i for i in issues if i['severity'] == 'HIGH'])
    medium = len([i for i in issues if i['severity'] == 'MEDIUM'])
    low = len([i for i in issues if i['severity'] == 'LOW'])
    
    print(f"\nTotal Issues Found: {len(issues)}")
    print(f"  {COLORS['HIGH']}High:   {high}{COLORS['RESET']}")
    print(f"  {COLORS['MEDIUM']}Medium: {medium}{COLORS['RESET']}")
    print(f"  {COLORS['LOW']}Low:    {low}{COLORS['RESET']}")
    
    if high > 0:
        print(f"\n{COLORS['HIGH']}⚠️  CRITICAL: {high} high-severity issue(s) found!{COLORS['RESET']}")
    elif len(issues) == 0:
        print(f"\n{COLORS['LOW']}✅ No security issues found! Good job!{COLORS['RESET']}")
    
    print("\n" + "="*50 + "\n")

def main():
    """Main function"""
    print_banner()
    
    print(f"[*] Region: {AWS_REGION}")
    print(f"[*] Starting security audit...\n")
    
    # Initialize and run S3 scanner
    s3_scanner = S3Scanner(region=AWS_REGION)
    issues = s3_scanner.scan_all_buckets()
    
    # Print all issues
    if issues:
        print(f"\n{'='*50}")
        print("SECURITY ISSUES FOUND")
        print('='*50)
        
        for issue in issues:
            print_issue(issue)
    
    # Print summary
    print_summary(issues)
    
    print("[*] Scan complete!")
    
    return 0 if len(issues) == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
