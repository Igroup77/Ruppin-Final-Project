﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Final_Project.Models;


namespace Final_Project.Controllers
{
    public class DashBoardsController : ApiController
    {
        //GET api/<controller>
        public DashBoard Get()
        {
            DashBoard dash = new DashBoard();
            return dash.ReadDashBoard();
            //dash.Patient = 1;
            //return dash;
        }

        //public int Get()
        //{
        //    return 1;
        //}



        // POST api/<controller>
        public void Post([FromBody]string value)
        {
        }

        // PUT api/<controller>/5
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/<controller>/5
        public void Delete(int id)
        {
        }
    }
}