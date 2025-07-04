# 1. Model Failure: 
*Your model underestimates delivery time on rainy days. Do you fix the model, the data, or the business expectations?*

If the model underestimates delivery time on rainy days, it's reasonable to assume the issue lies in the data, not the model or business expectations.
From a business perspective, rainy conditions are expected to increase delivery times due to factor such as reduced visibility, traffic congestion.
A model that shows the opposite is likely to be a data imbalance. for example, fewer deliveries occurring on rainy days, or rain being associated with shorter routes in the dataset.

As such, my first step would be to investigate and address the data:

- Check the class balance for Weather = Rainy.
- Analyze whether rain is disproportionately linked to short distances or preparation times.

# 2. Transferability: 
*The model performs well in Mumbai. It’s now being deployed in São Paulo. How do you ensure generalization?*

As this change introduces a new context for the model, the first step would be to analyze the data from São Paulo, especially the distribution of key features such as `Traffic_Level`, `Distance_km`.
It's also important to verify whether the operational processe are similar. If not, the model may require local calibration.

I would then collect a ground truth sample from São Paulo, run the current model on it, and compare the performance to the scores obtained in Mumbai. 
This would reveal any performance gap between the two cities.

If the gap is significant, I would:
- Fine-tune the model using São Paulo data, or
- Retrain the model using a combined dataset from both cities to improve generalization.

These steps help ensure the model adapts to the local dynamics of São Paulo while retaining what it has learned from Mumbai.

# 3. GenAI Disclosure: 
*Generative AI tools are a great resource that can facilitate development, what parts of this project did you use GenAI tools for? How did you validate or modify their output?*

Throughout this project, I used it as a support resource to enhance productivity and code quality.

I relied on it to guide me through the implementation of GridSearchCV and the learning curves graphs, especially when deciding on the best way to visualize and interpret model performance across different configurations. It also helped me refine the structure and wording of my reporting documents, making the explanations clearer.

Additionally, I used it to reorganize the codebase, splitting the pipeline into cleaner and more modular files, improving maintainability and adhering to good software development practices. In the process, it also assisted me in optimizing functions to follow the DRY (Don't Repeat Yourself) principle, making the entire code more concise and reusable.

To ensure the reliability of the output, I reviewed all code suggestions carefully, tested them locally, and adjusted them when necessary to fit the specific context of the dataset and project requirements. It served as a helpful collaborator, but the final decisions and implementations were always validated through experimentation, manual testing, and understanding of the methods involved.

# 4. Your Signature Insight: 
*What's one non-obvious insight or decision you're proud of from this project?*

I noticed that `Courier_Experience_yrs` received a strong positive coefficient in the Ridge model, even though its correlation with delivery time was very low. 
At first, this seemed contradictory and possibly erroneous but instead of removing the feature, I decided to look deeper. I realized this was a good example of how linear models can capture conditional relationships, not just simple correlations.
In this case, it made sense that more experienced couriers might be assigned longer or more complex deliveries, which could explain the higher delivery times.

# 5. Going to Production: 
*How would you deploy your model to production? What other components would you need to include/develop in your codebase? Please be as detailed each step of the process, and feel free to showcase some of these components in the codebase.*

For this particular case, where the goal is to predict delivery time for each individual order, I would deploy the model using a Dockerized API. This allows the model to respond in real time whenever a new delivery request is created, making it ideal for fast-paced logistics environments.

To start, I would implement an API endpoint using FastAPI, which is fast and integrates well with Pydantic for input validation. The API would receive the necessary features (such as distance, traffic level, vehicle type, etc), validate them automatically, load the serialized model pipeline, and return the estimated delivery time as a JSON response. This setup allows any internal or external system to access the model through a simple HTTP request.

Once the API is functional, I would containerize the service using Docker. The Dockerfile would define all dependencies, environment variables, and the entry point for the application. The resulting Docker image could then be pushed to the company's infrastructure, whether it's AWS, GCP, Azure, or another platform, making it easy to deploy consistently across environments.

To ensure code reliability and maintainability, I’d include unit tests that verify parts of the pipeline: confirming the model loads correctly, validating the structure and types of the inputs, and ensuring consistent prediction behavior. These tests can be run locally and integrated into a CI/CD pipeline to catch regressions early.

Altogether, this setup ensures the model is reliable, scalable, and ready for real-time predictions in a clean and maintainable way.