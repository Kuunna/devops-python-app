#!/bin/bash
echo "Testing local deployment..."
docker-compose up -d
sleep 5
curl http://localhost:5000
curl http://localhost:5000/health
docker-compose down