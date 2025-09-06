#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的SMTP邮件发送测试脚本
"""

import smtplib
import sys
import os
import argparse
from datetime import datetime
from email.mime.text import MIMEText

def send_email(to_email, from_email='test@example.com', 
               smtp_host='localhost', smtp_port=587):
    """发送测试邮件"""
    
    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 邮件内容
    subject = f"SMTP中继测试邮件 - {current_time}"
    body = f"""这是一封测试邮件。

发件人: {from_email}
收件人: {to_email}
SMTP服务器: {smtp_host}:{smtp_port}

如果您收到这封邮件，说明SMTP中继服务工作正常！
"""
    
    # 创建邮件
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    try:
        print(f"正在发送邮件到 {to_email}...")
        
        # 连接并发送
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.sendmail(from_email, [to_email], msg.as_string())
        server.quit()
        
        print("✓ 邮件发送成功!")
        return True
        
    except Exception as e:
        print(f"✗ 发送失败: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='发送SMTP测试邮件')
    parser.add_argument('to_email', help='收件人邮箱地址')
    parser.add_argument('--from-email', default='test@example.com', 
                       help='发件人邮箱地址 (默认: test@example.com)')
    parser.add_argument('--smtp-host', 
                       default=os.getenv('SMTP_HOST', 'localhost'),
                       help='SMTP服务器地址 (默认: localhost, 可通过SMTP_HOST环境变量设置)')
    parser.add_argument('--smtp-port', type=int,
                       default=int(os.getenv('SMTP_PORT', '2525')),
                       help='SMTP服务器端口 (默认: 2525, 可通过SMTP_PORT环境变量设置)')
    
    args = parser.parse_args()
    
    print(f"配置信息:")
    print(f"  发件人: {args.from_email}")
    print(f"  收件人: {args.to_email}")
    print(f"  SMTP服务器: {args.smtp_host}:{args.smtp_port}")
    print()
    
    success = send_email(args.to_email, args.from_email, args.smtp_host, args.smtp_port)
    sys.exit(0 if success else 1)
