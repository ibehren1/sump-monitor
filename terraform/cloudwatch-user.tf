resource "aws_iam_user" "cloudwatch" {
  name = "cloudwatch"
  path = "/"
  tags = {}
}

resource "aws_iam_access_key" "cloudwatch_key" {
  user = aws_iam_user.cloudwatch.name
}

output "cloudwatch_access_key" {
  description = "cloudwatch user access_key"
  value       = aws_iam_access_key.cloudwatch_key.*.id
}
output "cloudwatch_access_secret" {
  description = "cloudwatch user access_secret"
  value       = aws_iam_access_key.cloudwatch_key.secret
}

resource "aws_iam_policy_attachment" "cloudwatch-policy-attachment" {
  name       = "cloudwatch-policy-attachment"
  users      = [aws_iam_user.cloudwatch.name]
  policy_arn = aws_iam_policy.cloudwatchPolicy.arn
}
