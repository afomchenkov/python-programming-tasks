import asyncio

async def test_port(host, port, timeout=3):
    coro = asyncio.open_connection(host, port)
    
    try:
        _, writer = await asyncio.wait_for(coro, timeout)
        writer.close()
        return True, port
    except (asyncio.TimeoutError, ConnectionRefusedError):
        return False, port
    
    
async def main(host, ports):
    print(f"Scanning ports on {host}...")
    coros = [test_port(host, port) for port in ports]
    
    for coro in asyncio.as_completed(coros):
        success, port = await coro
        if success:
            print(f"Port {host}:{port} [OPEN]")
        else:
            # print(f"Port {port} is closed or filtered.")
            pass
            
if __name__ == '__main__':
    host = 'python.org'
    ports = range(1, 1024)
    asyncio.run(main(host, ports))