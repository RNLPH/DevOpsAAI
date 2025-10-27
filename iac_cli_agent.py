import sys

# Simple intent parser and code generator
def generate_terraform_code(prompt):
    prompt = prompt.lower()
    if "ec2" in prompt:
        return """resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "ExampleEC2"
    
  }
}"""
    elif "s3" in prompt:
        return """resource "aws_s3_bucket" "example" {
  bucket = "example-bucket"
  acl    = "private"
}"""
    elif "vpc" in prompt:
        return """resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "ExampleVPC"
  }
}"""
    else:
        return "Sorry, I can't generate code for that request yet."

# Main CLI loop
if __name__ == "__main__":
    print("Welcome to the IaC CLI Agent!")
    prompt = input("Enter your infrastructure request: ")
    code = generate_terraform_code(prompt)
    print("\nGenerated Terraform Code:\n")
    print(code)