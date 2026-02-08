💡 Usage Examples
Scan Specific Region 

# Edit config.py
AWS_REGION = 'eu-west-1'  # Change region

# Run scan
python auditor.py 

Scan Multiple AWS Accounts
# Configure profile for second account
aws configure --profile production

# Modify auditor.py to use profile
# boto3.Session(profile_name='production')

Save Results to File
python auditor.py > scan_results.txt 

........................................................

🐛 Troubleshooting
Common Issues
Issue: AccessDenied error when scanning
# Solution: Ensure IAM user has SecurityAudit policy
aws iam attach-user-policy --user-name security-auditor \
  --policy-arn arn:aws:iam::aws:policy/SecurityAudit 


  Issue: No buckets found
# Solution: Check AWS region configuration
aws s3 ls --region us-east-1

Issue: ModuleNotFoundError: No module named 'boto3'
# Solution: Install dependencies
pip install -r requirements.txt

📚 Learning Resources
AWS Security Best Practices

AWS Security Best Practices
CIS AWS Foundations Benchmark
OWASP Cloud Security Top 10

Python & boto3

boto3 Documentation
AWS SDK Examples

Pentesting Resources

AWS Penetration Testing
Cloud Security Alliance 


MIT License

Copyright (c) 2026 Farhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
