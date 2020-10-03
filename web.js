console.clear()
const log = console.log
const path = require('path')
const hapi = require('hapi')
const inert = require('inert')
// Маршруты могут быть сконфигурированы для объекта сервера
const server = new hapi.Server({
  port: 10101,
  routes: {
 files: {
 relativeTo: path.join(__dirname, 'public')
 }
  }
})
const init = async () => {
  // Команда server.register() добавляет плагин для приложения
  await server.register(inert)
  // inert добавляет обработчик папок, чтобы 
  // указать маршрут для обслуживания нескольких файлов
  server.route({
 method: 'GET',
 path: '/{param*}',
 handler: {
 directory: {
 path: '.',
 redirectToSlash: true,
 index: true
 }
 }
  })
  await server.start()
}
init()
log('\x1b[32m', '    -----------------------    ')
log('\x1b[32m', '       Server is running       ')
log('\x1b[32m', '    -----------------------    ')
