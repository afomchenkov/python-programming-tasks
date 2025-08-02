import asyncio

"""
Execute external program as a subprocess:
- asyncio.create_subprocess_exec()
- asyncio.create_subprocess_shell()

Both functions return a asyncio.subprocess.Process object that can
be used to interact with the subprocess.

process = await asyncio.create_subprocess_exec('echo', 'Hello, World!',)
"""

async def main():
    process1 = await asyncio.create_subprocess_exec(
        'echo', 'Hello, World!',
        # stdout=asyncio.subprocess.PIPE,
        # stderr=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    
    print('Process started:', process1.pid)
    _ = await process1.communicate(b'[Hello World]\n')
    await process1.wait()
    
    process2 = await asyncio.create_subprocess_shell(
        'echo "Hello from shell!"',
        stdin=asyncio.subprocess.PIPE,
    )
    print('Shell process started:', process2.pid)
    
    data, _ = await process1.communicate()
    # print('Output:', data.decode().strip())
    # terminate the first process if needed - SIGTERM signal
    # process1.terminate()
    # kill the process if needed - SIGKILL signal
    # process.kill()
    
    await process2.wait()
    
    # open socket connection
    # reader, writer = await asyncio.open_connection(host=, port=,)
    # ports:
    #  - 80 - HTTP
    # - 443 - HTTPS
    # - 22 - SSH
    # - 23 - SMTP
    # reader, writer = await asyncio.open_connection('www.google.com, 443, ssl=True)
    # start the server
    # 
    # async def handler(reader, writer):
    #     data = await reader.read(100)
    #     message = data.decode()
    #     addr = writer.get_extra_info('peername')
    #     print(f"Received {message!r} from {addr!r}")
    #     print('Send: Hello World!')
    #     writer.write(b'Hello World!\n')
    #     await writer.drain()
    #     print('Closing the connection')
    #     writer.close()
    #     await writer.wait_closed()
    # server = await asyncio.start_server(handler, host='localhost', port=8888)
   

if __name__ == '__main__':
    asyncio.run(main())
    
    print('Subprocess execution completed.')
