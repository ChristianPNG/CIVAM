import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {

  constructor() { }

  public missionCollapsed = true;
  public originCollapsed = true;
  public peopleCollapsed = true;
  ngOnInit(): void {
  }

}



