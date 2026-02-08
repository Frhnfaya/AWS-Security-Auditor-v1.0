
 # S3 Security Scanner 
import boto3
from botocore.exceptions import ClientError

class S3Scanner:
    def __init__(self, region='us-east-1'):
        """Initialize S3 scanner with AWS region"""
        self.s3_client = boto3.client('s3', region_name=region)
        self.issues = []
    
    def scan_all_buckets(self):
        """Scan all S3 buckets for security issues"""
        print("\n[*] Starting S3 bucket scan...")
        
        try:
            # Get list of all buckets
            response = self.s3_client.list_buckets()
            buckets = response.get('Buckets', [])
            
            if not buckets:
                print("[!] No S3 buckets found")
                return self.issues
            
            print(f"[*] Found {len(buckets)} bucket(s). Scanning...\n")
            
            # Scan each bucket
            for bucket in buckets:
                bucket_name = bucket['Name']
                self.scan_bucket(bucket_name)
            
            return self.issues
            
        except ClientError as e:
            print(f"[!] Error listing buckets: {e}")
            return self.issues
    
    def scan_bucket(self, bucket_name):
        """Scan individual bucket for security issues"""
        print(f"[*] Scanning bucket: {bucket_name}")
        
        # Check 1: Public Access
        self.check_public_access(bucket_name)
        
        # Check 2: Encryption
        self.check_encryption(bucket_name)
        
        # Check 3: Versioning
        self.check_versioning(bucket_name)
    
    def check_public_access(self, bucket_name):
        """Check if bucket is publicly accessible"""
        try:
            acl = self.s3_client.get_bucket_acl(Bucket=bucket_name)
            
            for grant in acl.get('Grants', []):
                grantee = grant.get('Grantee', {})
                uri = grantee.get('URI', '')
                
                # Check for public access
                if 'AllUsers' in uri or 'AuthenticatedUsers' in uri:
                    self.issues.append({
                        'bucket': bucket_name,
                        'severity': 'HIGH',
                        'issue': 'Public Access Enabled',
                        'description': f'Bucket is publicly accessible to {grantee.get("Type")}'
                    })
                    return
                    
        except ClientError as e:
            print(f"    [!] Could not check public access: {e}")
    
    def check_encryption(self, bucket_name):
        """Check if bucket has encryption enabled"""
        try:
            self.s3_client.get_bucket_encryption(Bucket=bucket_name)
            # If no error, encryption is enabled (good!)
            
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                self.issues.append({
                    'bucket': bucket_name,
                    'severity': 'MEDIUM',
                    'issue': 'Encryption Not Enabled',
                    'description': 'Bucket does not have server-side encryption enabled'
                })
    
    def check_versioning(self, bucket_name):
        """Check if bucket has versioning enabled"""
        try:
            response = self.s3_client.get_bucket_versioning(Bucket=bucket_name)
            status = response.get('Status', 'Disabled')
            
            if status != 'Enabled':
                self.issues.append({
                    'bucket': bucket_name,
                    'severity': 'LOW',
                    'issue': 'Versioning Not Enabled',
                    'description': 'Bucket versioning is disabled (data recovery risk)'
                })
                
        except ClientError as e:
            print(f"    [!] Could not check versioning: {e}")
    
    def get_issues(self):
        """Return all found issues"""
        return self.issues
