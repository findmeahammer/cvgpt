from django.conf import settings
import os
from openai import OpenAI

client = OpenAI()
client = OpenAI(
  api_key=settings.OPENAI_API_KEY,
)
# print("API KEY:" + settings.OPENAI_API_KEY)


def get_completion(prompt):

    # print("key:" + client.api_key)
    completion = client.chat.completions.create(
     model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful giving information and answering questions about Matt Cresswell, keep your answers concise. You will recieve the resume for Matt next"},
    {"role": "system", "content": get_resume("matt")},
    {"role": "user", "content": prompt}
    ] 
    )
    
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def get_resume(person):
    cv ="""
    Matt's core beliefs:
    - People come before technology, automate everything except communication with people
    - That most people are trying to do their best, however often lack the experience and knowledge to attain their best
    - An unattainable goal is better than no goal at all; continuous delivery should be the goal for all development workflows
    - The cloud is someone else's computer; keep an eye on costs, tag everything, and define your boundaries
    - Security and testing are as important as the feature, often more so
    - Be honest and open with your peers and the wider business

    Work history:
    May 2022 to present: Berkeley Payment Solutions as VP of Technology
    Berkeley Payment is a real-time payment and card provider based in Ontario, Canada. They provide a single high performance API and white labeled solution to small-medium businesses looking for
    physical/virtual cards and payments. 50 employees, 1,000+ customers.
    As VP of Technology he rebuilt the technology team, defined new processes, patterns, and technology standards. Regain the business trust in Technology
    through transparency and the adoption of DORA metrics to measure the technology team.
    In addition:
    ■ Addressed operational issues impacting feature delivery with ring fenced operational teams. Utilized global, flexible offshore
teams to supplement the in house team. Implemented SFIA skills framework for career growth.
■ Migrated from Oracle Cloud to AWS, created the patterns and tools to move all infrastructure with Terraform, Kubernetes (EKS,
ArgoCD, Athena, Python).
■ Transitioned the organization towards PCI 4.0 compliance with a shift to DevSecOps model, updated security practices and
processes within Technology and across the organisation.
■ Reduced costs by leveraged partners for specialist roles across security and infrastructure to negate the need to have dedicated
roles in the team.
■ Introduced low-code python solutions with Generative AI to improve and automate internal workflows

    August 2021 to May 2022: Sensibill as Director of Engineering
    Sensibill is a data focussed start-up, seeking to improve financial wellness through personal spending insights for 60+ million users

    As Director of engineering matt reported to the CTO, moved to an expanded role managing the API (node.js, python) , SDK teams (native Android/iOS) and ML
pipelines, with the primary goal of providing the best integration experience possible for customers.
    """
    return cv