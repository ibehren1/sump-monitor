resource "aws_iam_policy" "cloudwatchPolicy" {
  name = "cloudwatchPolicy"
  path = "/"
  policy = jsonencode(
    {
      Statement = [
        {
          Action = [
            "cloudwatch:PutMetricData"
          ]
          Effect   = "Allow"
          Resource = "*"
        },
      ]
      Version = "2012-10-17"
    }
  )
}
