# Operationalizing Machine Learning in Azure

## Table of Contents
   * [Overview](#Overview)
   * [Architectural Diagram](#Architectural-Diagram)
   * [Key Steps and Screenshots](#Key-Steps-and-Screenshots)
   * [Screen Recording](#Screen-Recording)
   * [Comments and future improvements](#Comments-and-future-improvements)
   * [References](#References)

***

## Overview

The goal of this project is to explore how we would train a machine learning model in Azure and then put it into production. 

In the first part of the project, we will start by training, deploying, and consuming a machine learning model in Azure with AutoML. The Azure Machine Learning Studio interface will be used to train and deploy the best model, which creates a REST API endpoint. Finally, we'll use our Command-Line Interface (CLI) to consume the model with [Swagger](https://swagger.io/).

In the second part, we will create a pipeline that trains a machine learning model and puts it into production using a Jupyter Notebook and the Azure Python SDK.

We use a dataset that contains data regarding direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit, based on features such as age, job, marital status, and education. The dataset can be found here: [Bank Marketing dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing).

***

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

Our project will follow the following steps:

![Steps to Operationalizing ML](./images/steps-to-operationalizing-ml.png)

***

## Key Steps and Screenshots

We will now go through the key steps of the entire project.

### **1. Authentication** 

Authentication is important for giving users different levels of privileges. In our case, we are using the Udacity workspace, so we cannot create a Service Principal. Therefore, can skip this step.

### **2. Automated ML Experiment (AutoML)** 

AutoML allows you to automatically run a series of different machine learning algorithms and parameters for you. In this project, we provide AutoML some custom configurations, run it, then choose the best model.

### **3. Deploy the best model** 

Deploying means that we are creating an endpoint (in this case, REST API) that allows us to interact with the HTTP API service. For this project, we will allow the HTTP API service to interact with the best AutoML model by sending POST requests to the endpoint.

### **4. Enable logging** 

In Azure, we can enable logging by enabling Application Insights. Application Insights is a useful tool to detect anomalies and visualize performance of our deployed model. We can enable Application Insights when we are deploying our model, but we will enable it via our CLI for this project.

### **5. Swagger Documentation** 

Swagger is a framework for describing an API using a common language that everyone can understand. Azure provides a Swagger JSON file for deployed models that can look up in your IDE or in the Swagger UI. Any mistakes are flagged, and alternatives are suggested. At the heart of Swagger is its specification. The Swagger specification is the rulebook that standardizes API practices (how to define parameters, paths, responses, models, etc). And every other part of Swagger is just a way of appropriating or creating API documentation that works with these rules. Reference: [What is Swagger and Why Does it Matter?](https://blog.readme.com/what-is-swagger-and-why-it-matters/)

### **6. Consume model endpoints** 

Here we perform model inference in our local CLI by using the REST endpoint URL and Primary Key (for authentication) of our deployed model.

### **7. Create and publish a pipeline** 

An important part of MLOps is to automate workflows via Pipelines. For this project, we will be using a Pipeline to automate the entire process (minus step 4 and 5). Creating a pipeline via the Azure Python SDK is useful allows us to automate the process and share our steps with colleagues.

***

## Screen Recording

Here's a link to a video explaining the different parts of the project: [Operationalizing ML Screencast - Jacques T](https://www.youtube.com/watch?v=mH5c6UD4-Vk&feature=youtu.be)
