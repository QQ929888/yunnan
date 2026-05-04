const mysql = require('mysql2/promise');

const pool = mysql.createPool({
    host: '47.108.20.237',
    port: 3306,
    user: 'root',
    password: '123456@xqxayjr',
    database: 'web_auth',
    connectionLimit: 10
});

module.exports = pool;