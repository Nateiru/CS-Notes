#### 2022/3/17

SSH（Secure Shell）是一种安全协议，用于远程访问和管理计算机系统。SSH支持多种认证协议，包括以下几种：

1. 密码认证：用户使用用户名和密码登录到SSH服务器。
2. **公钥认证**：使用公钥密码对进行身份验证。客户端和服务器之间的通信会使用加密算法对密码进行保护。
3. **Kerberos认证**：Kerberos是一种网络身份验证协议，可用于通过SSH进行身份验证。在Kerberos中，客户端和服务器都有自己的密钥，并且双方之间的通信使用加密算法进行保护。

> `GSSAPIAuthentication`是SSH客户端和服务器的配置选项之一，用于启用基于GSSAPI的身份验证。GSSAPI（Generic Security Services Application Program Interface）是一种标准化的API，用于提供安全性和数据完整性，它是一种通用的安全性框架，用于支持各种身份验证和密钥交换机制。
>
> ```bash
> GSSAPIAuthentication yes
> ```
>
> 在启用了`GSSAPIAuthentication`之后，SSH客户端将尝试使用Kerberos等身份验证协议进行身份验证，如果未安装或未配置Kerberos，则会自动降级到基本的用户名和密码身份验证。如果成功进行了GSSAPI身份验证，则可以使用SSH代理来访问其他远程主机，而无需再次输入身份验证信息。

#### 2022/3/20

1. ssh-keygen 生成密钥对
2. 将公钥配置的 GitLab（开发仓库） 和 Gerrir（Code View）
3. 配置SSH Config（主要用于更改ssh主机名） 和 Git Config（name和email 重命名url名称）

同事开挂获得 su 权限使用 brew 下载软件