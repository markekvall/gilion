import React, { useEffect, useState} from 'react';
import axios from "axios";
import { Grid, Paper, Typography } from '@mui/material';
import Box from "@mui/material/Box"
import { Scrollbar } from 'react-scrollbars-custom';

import Button from "@mui/material/Button"

interface Data {
    response: string;
}

const Home: React.FC = () => {
    const [data, setData] = useState<Data[]>([]);
    const [error, setError] = useState<string | null>(null);

    const fetchData = async () => {

        console.log('hello');
        try {
            console.log('Fetching data...');
    
            const response = await axios.get('http://localhost:8000');
            const message = response.data.message; // Update to access 'message' directly
            console.log('Response received:', response.data);
            setData([{ response: message }]);
            setError(null); // Reset error if previous request was successful
        } catch (error) {
            console.error('Error fetching data:', error);
            setError('Failed to fetch data');
        }
    };

    const testFetchData = async () => {

        console.log('hellolog');
        //setData([{ response: 'hello' }]);
        const response = await axios.get('http://localhost:8000');
        const message = response.data.message; // Update to access 'message' directly
        console.log('Response received:', response.data);
        setData([{ response: message }]);
        
    };

    return (
        <Grid
            container
            direction="column"
            justifyContent="center"
            alignItems="center"
            style={{ minHeight: '100vh', height: '100%' }} 
        >
            <Box
                sx={{
                    width: '500px',
                    height: '800px',
                    borderRadius: '30px',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                }}
            >
                <Paper
                sx={{
                    width: '100%',
                    height: '100%',
                    padding: '20px',
                    borderRadius: '25px',
                    textAlign: 'center',
                }}
                >
                <Grid container direction="column" spacing={2} alignItems="center" padding="20px">
                    <Typography variant="h5" gutterBottom >
                    YOUR DATA
                    </Typography>


                    <Button variant="contained" onClick={testFetchData} style={{ marginBottom: '20px' }}>
                    Fetch data
                    </Button>
                    
                    {data.map((item, index) => (
                        <Typography key={index} variant="body1">{item.response}</Typography>
                        ))}

                    
                </Grid>
                </Paper>
            </Box>
        </Grid>
    );
};



export default Home;