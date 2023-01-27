"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
// Require the framework and instantiate it
const static_1 = __importDefault(require("@fastify/static"));
const fastify_1 = __importDefault(require("fastify"));
const path_1 = __importDefault(require("path"));
const server = (0, fastify_1.default)({ logger: true });
server.register(static_1.default, {
    root: path_1.default.join(__dirname, "../public")
});
// Declare a route
server.get('/', async (request, reply) => {
    return { hello: 'world' };
});
// Run the server!
const start = async () => {
    try {
        await server.listen({ port: 3000 });
    }
    catch (err) {
        server.log.error(err);
        process.exit(1);
    }
};
start();
