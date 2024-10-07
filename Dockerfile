# Use an official Node.js image as the base image (modify as needed based on your app)
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port your app runs on
EXPOSE 3000

# Start the Wisecow app
CMD ["npm", "start"]

