import socket
import re
# Examples
# get_open_ports("209.216.230.240", [440, 445])
# get_open_ports("www.stackoverflow.com", [79, 82])

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    ip = ""
    # Argument
    # target : URL or IP address
    # port_range : list of two numbers indicating the first and last
    # verbose : if it is true, return a descriptive string

    # URL or IP address
    # url is invalid
    # return "Error:Invalid hostname"

    # IPaddress is invalid
    # return "Error:Invalid IP address"
    # URL or IP address validation

    try:
        ip = socket.gethostbyname(target)
        # ポートスキャン
        for port in range(port_range[0], port_range[1] + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
    except KeyboardInterrupt:
        return "error"
    except socket.gaierror:
        if (re.search('[a-zA-Z]', target)):
            return "Error: Invalid hostname"
        return "Error: Invalid IP address"
    except socket.error:
        return "Error: Invalid IP address"

    # ホスト名の取得
    try:
        host = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        host = None
        
    # ヘッダー
    # result = f"Open ports for {host if host else ip} ({ip})\nPORT     SERVICE\n"

    result = "Open ports for"
    if host != None:
        result += f" {host} ({ip})"
    else:
        result += f" {ip}"
    result += "\n"

    if verbose:
        result += "PORT     SERVICE\n"
        # ポートリスト
        for port in open_ports:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "unknown"
            result += f"{port:<8} {service}\n"

        return result.strip()  # 最後の `\n` を削除
    else:
        return open_ports

    return (open_ports)

    # Return : verbose = true
    # Open ports for {URL} ({IP address})
    # PORT     SERVICE
    # {port}   {service name}
    # {port}   {service name}

    # Return : verbose = false
    # The function should return a list of open ports in the given range.
