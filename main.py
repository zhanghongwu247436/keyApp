from flask import Flask, render_template, request  
app = Flask(__name__)

# 首页路由：渲染主页 index.html | Home route: render index.html
@app.route('/')
def index():
    return render_template('index.html')

# 导入比特币库 | Import bitcoin library
import bitcoin as byc
import hashlib

# 创建随机私钥接口 | Generate random private key API
@app.route('/create')
def do_create():
    return byc.random_key()

# 处理所有密钥转换命令 | Handle all key conversion commands
@app.route('/doGet')
def do_get():
    # 获取前端传入的私钥和命令 | Get private key and command from frontend
    prik = request.args['prik']
    cmd = request.args['cmd']

    # 1、转为压缩私钥 | Convert to compressed private key
    if cmd == 'toPrikComp':
        return prik + '01'

    # 2、私钥转 WIF 格式 | Convert private key to WIF format
    elif cmd == 'toPrikWif':
        return byc.encode_privkey(prik, 'wif')

    # 3、私钥转普通公钥 | Convert private key to uncompressed public key
    elif cmd == 'toPubk':
        return byc.privtopub(prik)

    # 4、私钥转压缩公钥 | Convert private key to compressed public key
    elif cmd == 'toPubkComp':
        return byc.compress(byc.privtopub(prik))

    # 5、私钥转公钥哈希 (RIPEMD160) | Convert private key to public key hash
    elif cmd == 'toPubkHash':
        pubk = byc.privtopub(prik)
        return byc.hash160(byc.safe_from_hex(pubk))

    # 6、私钥转普通地址 | Convert private key to uncompressed address
    elif cmd == 'toAddr':
        return byc.pubtoaddr(byc.privtopub(prik))

    # 7、私钥转压缩地址 | Convert private key to compressed address
    elif cmd == 'toAddrComp':
        return byc.pubtoaddr(byc.compress(byc.privtopub(prik)))

    # 未知命令 | Unknown command
    else:
        return "Invalid command"

## Hw2: Implements the rests of 'cmd'.
#--------------------------------------------------

if __name__ == '__main__':
    app.run(port=8080, debug=True)
