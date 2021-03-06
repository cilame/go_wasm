

with open('./lib.wasm', 'rb') as f:
    s = f.read()

v = ''.join([('0' + hex(i)[2:])[-2:] for i in s])

a = r'''WebAssembly.instantiate(new Uint8Array(`'''
b = r'''`.match(/[a-z0-9A-Z]{2}/g).map(function(e){return parseInt(e, 16)})), {wasi_unstable:{fd_write:function(){}}}).then(function (obj) {
    wasm = obj.instance;
})'''
s = a + v + b
print(s)