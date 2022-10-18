import { ModelInit, MutableModel } from "@aws-amplify/datastore";

type UserMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type AgentMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type UserAgentMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

export declare class User {
  readonly id: string;
  readonly name?: string | null;
  readonly Orders?: (UserAgent | null)[] | null;
  readonly createdAt?: string | null;
  readonly updatedAt?: string | null;
  constructor(init: ModelInit<User, UserMetaData>);
  static copyOf(source: User, mutator: (draft: MutableModel<User, UserMetaData>) => MutableModel<User, UserMetaData> | void): User;
}

export declare class Agent {
  readonly id: string;
  readonly name: string;
  readonly gender?: string | null;
  readonly locations: (string | null)[];
  readonly Orders?: (UserAgent | null)[] | null;
  readonly createdAt?: string | null;
  readonly updatedAt?: string | null;
  constructor(init: ModelInit<Agent, AgentMetaData>);
  static copyOf(source: Agent, mutator: (draft: MutableModel<Agent, AgentMetaData>) => MutableModel<Agent, AgentMetaData> | void): Agent;
}

export declare class UserAgent {
  readonly id: string;
  readonly user: User;
  readonly agent: Agent;
  readonly createdAt?: string | null;
  readonly updatedAt?: string | null;
  constructor(init: ModelInit<UserAgent, UserAgentMetaData>);
  static copyOf(source: UserAgent, mutator: (draft: MutableModel<UserAgent, UserAgentMetaData>) => MutableModel<UserAgent, UserAgentMetaData> | void): UserAgent;
}