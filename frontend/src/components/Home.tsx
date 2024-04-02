import React, { useEffect, useState} from 'react';
import axios from "axios";
import { Grid, Paper, Typography } from '@mui/material';
import Box from "@mui/material/Box"
import { Scrollbar } from 'react-scrollbars-custom';
import Button from "@mui/material/Button"


interface Data {
    date: string;
    country_code: string;
    A: number;
    B: number;
    C: number;
}


const Home: React.FC = () => {
    const [data, setData] = useState<Data[]>([]);
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [countryCode, setCountryCode] = useState('');
    const [fetchType, setFetchType] = useState('daily'); 
    const username = 'Alice';
    const password = 'My Very Secret Password';
    ///const url = `http://localhost:8000/fetch-${fetchType}?start_date=${startDate}&end_date=${endDate}&country_code=${countryCode}`;



    const fetchFilteredData = async () => {
        const url = `http://localhost:8000/fetch-${fetchType}`;
        const queryParams = {
            start_date: startDate,
            end_date: endDate,
            country_code: countryCode
        };
    
        try {
            const response = await axios.get(url, {
                params: queryParams,
                auth: {
                    username: username,
                    password: password
                }
            });
            const jsonData = JSON.parse(response.data.company_data) as Data[];
            setData(jsonData)
        } catch (error) {
            console.error('Error:', error);
        }
        
    };

    const fetchInitialData = async () => {
        const url = `http://localhost:8000`;
        
        try {
            const response = await axios.get(url, {
                auth: {
                  username: username,
                  password: password
                }
            });
            const jsonData = JSON.parse(response.data.company_data) as Data[];
            setData(jsonData)
        } catch (error) {
            console.error('Error:', error);
        }
        
    };

    
    useEffect(() => {
        fetchInitialData();
    }, []); 


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
                    width: '1000px',
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

                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}>
                        <label style={{ marginRight: '10px' }}>Start Date:</label>
                        <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} style={{ marginRight: '20px' }} />
                        <label style={{ marginRight: '10px' }}>End Date:</label>
                        <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} style={{ marginRight: '20px' }} />
                        <label style={{ marginRight: '10px' }}>Country Code:</label>
                        <input type="text" value={countryCode} onChange={(e) => setCountryCode(e.target.value)} style={{ marginRight: '20px' }} />
                        <label style={{ marginRight: '10px' }}>Fetch Type:</label>
                        <select value={fetchType} onChange={(e) => setFetchType(e.target.value)} style={{ marginRight: '20px' }}>
                            <option value="daily">Daily</option>
                            <option value="monthly">Monthly</option>
                        </select>
                    </div>

                    <Button variant="contained" onClick={fetchFilteredData} style={{ marginBottom: '20px' }}>
                    Fetch data
                    </Button>

                    <Scrollbar style={{ width: '100%', height: '60vh'}}>
                        {data.map((item, index) => (
                            <div key={index}>
                                <Typography variant="body1">Date: {item.date}, Country Code: {item.country_code}, A: {item.A}, B: {item.B}, C: {item.C}</Typography>

                            </div>
                        ))}
                    </Scrollbar>
                </Grid>
                </Paper>
            </Box>
        </Grid>
    );
};



export default Home;