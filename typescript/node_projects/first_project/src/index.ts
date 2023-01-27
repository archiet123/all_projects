// Require the framework and instantiate it
import fastifyStatic from "@fastify/static"
import fastify  from "fastify"
import path from "path"
const server = fastify({logger:true})
server.register(fastifyStatic,{
    root: path.join(__dirname, "../public")
})
// Declare a route
server.get('/', async (request, reply) => {
  return { hello: 'world' }
})

// Run the server!
const start = async () => {
  try {
    await server.listen({ port: 3000 })
  } catch (err) {
    server.log.error(err)
    process.exit(1)
  }
}
start()