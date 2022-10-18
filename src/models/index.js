// @ts-check
import { initSchema } from '@aws-amplify/datastore';
import { schema } from './schema';



const { User, Agent, UserAgent } = initSchema(schema);

export {
  User,
  Agent,
  UserAgent
};