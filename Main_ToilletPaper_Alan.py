from Agente_ToilletPaper import ToilletPaperAg
from Enviroment_ToilletPaper import ToilletPaperEnv

env1 = ToilletPaperEnv(10,2000,10000)

#env2 = ToilletPaperEnv(10,2000,5000)

agent1 = ToilletPaperAg(env1)

#agent2 = ToilletPaperAg(env2)

for i in range(20):
    action1 = agent1.act(env1)
    env1.change_state(action1)
    '''action2 = agent2.act(env2)
    env2.change_state(action2)'''
