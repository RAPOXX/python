const http = require('http')
const porta = 8080
http.createServer((res,req) => {
    console.log('servidor rodando na porta ' + porta)
    
}).listen(porta)



