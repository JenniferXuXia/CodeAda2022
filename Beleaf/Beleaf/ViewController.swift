//
//  ViewController.swift
//  Beleaf
//
//  Created by Sophia Liu on 10/16/22.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var profileImage: UIImageView!
    @IBOutlet weak var tomato4Image: UIImageView!
    @IBOutlet weak var tomato3Image: UIImageView!
    @IBOutlet weak var tomato2Image: UIImageView!
    @IBOutlet weak var tomatoImage: UIImageView!
    @IBOutlet weak var dockView: UIView!
    @IBOutlet weak var whiteView: UIView!
    @IBOutlet weak var extraView: UIView!
    @IBOutlet weak var indicatorView: UIView!
    @IBOutlet weak var buttonToSegue: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        profileImage.layer.cornerRadius = 60
        tomatoImage.layer.cornerRadius = 35
        tomato2Image.layer.cornerRadius = 35
        tomato3Image.layer.cornerRadius = 35
        tomato4Image.layer.cornerRadius = 35
        whiteView.layer.cornerRadius = 45
        dockView.layer.cornerRadius = 20
        extraView.layer.cornerRadius = 33
        indicatorView.layer.cornerRadius = 5
        
        
    }


}

